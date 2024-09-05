from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from services.django_api import DjangoAPI
from keyboards.default import main_menu_keyboard

router = Router()

# Класс для хранения состояний FSM
class RegistrationStates(StatesGroup):
    waiting_for_username = State()

# Обработчик состояния ожидания имени пользователя
@router.message(RegistrationStates.waiting_for_username)
async def process_username(message: Message, state: FSMContext):
    username = message.text.strip()
    
    # Проверка на валидность имени пользователя
    if not username:
        await message.answer("Пожалуйста, введите действительное имя пользователя.")
        return

    # Регистрация пользователя через Django API
    django_api = DjangoAPI()
    success = await django_api.register_user(message.from_user.id, username)
    await django_api.close()

    # Обработка успешной/неудачной регистрации
    if success:
        await message.answer(
            "Регистрация прошла успешно! Добро пожаловать в дневник аллергика.",
            reply_markup=main_menu_keyboard()
        )
        await state.clear()  # Очистка состояния
    else:
        await message.answer("Произошла ошибка при регистрации. Попробуйте позже.")
        await state.clear()  # Очистка состояния при ошибке

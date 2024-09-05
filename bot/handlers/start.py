from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from services.django_api import DjangoAPI
from keyboards.default import main_menu_keyboard, register_keyboard
from handlers.registration import RegistrationStates

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    django_api = DjangoAPI()
    is_registered = await django_api.is_user_registered(message.from_user.id)
    await django_api.close()

    if is_registered:
        await message.answer(
            "Добро пожаловать обратно! Что вы хотите сделать?",
            reply_markup=main_menu_keyboard()
        )
    else:
        await message.answer(
            "Привет! я бот для контроллирования аллергии. Похоже, ты еще не зарегистрирован. Давай начнем регистрацию.",
            reply_markup=register_keyboard()
        )
        await state.set_state(RegistrationStates.waiting_for_username)

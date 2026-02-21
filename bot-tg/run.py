import logging

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters.command import Command, CommandStart
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from openai import OpenAI
import os
import telegramify_markdown
import telegramify_markdown.customize as customize
customize.strict_markdown = False

# Настройка ключей
TELEGRAM_TOKEN = os.getenv('TG_TOKEN')

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'), base_url=os.getenv('OPENAI_API_BASE_URL'))

# Логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я бот с ИИ. Задавай вопрос.")

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    # Запрос к OpenAI (модель gpt-3.5-turbo или gpt-4)
    response = client.chat.completions.create(
        model="Qwen/Qwen3-0.6B",
        messages=[
        {"role": "system", "content": "Вы полезный помощник, который отвечает в Markdown."},
        {"role": "user", "content": user_text}]
    )

    answer = response.choices[0].message.content
    # answer = f"```markdown\n{response.choices[0].message.content}\n```"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=answer, parse_mode='Markdown')
    # await context.bot.send_message(chat_id=update.effective_chat.id, text=answer)

if __name__ == '__main__':
    
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    start_handler = CommandHandler('start', start)
    chat_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), chat)

    application.add_handler(start_handler)
    application.add_handler(chat_handler)

    application.run_polling()
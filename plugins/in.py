from pyrogram import Client, filters
from PIL import Image


Client.on_message(filters.command('image'))
async def image_handler(client, message):
    text = message.text.split(' ', 1)[1]  # Get the text after the command
    username = message.from_user.username  # Get the username of the user who sent the message

    # Convert the text to an image
    image = Image.new('RGB', (100, 50), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), text, fill=(0, 0, 0))

    # Save the image to a buffer
    buffer = BytesIO()
    image.save(buffer, format='PNG')
    buffer.seek(0)

    # Send the image to the user
    await client.send_photo(
        message.chat.id, 
        buffer, 
        caption=f"Image generated for {username}")

class Translation(object):
    START_TEXT = """Hey 👋,

<b>I'm a File Renamer Bot with permanent Thumbnail support!</b>

<b>Send me any Telegram file and reply to that file to /rename New Name.mkv</b>

Use /help for more details."""
    RENAME_403_ERR = "Sorry. You are not permitted to rename this file."
    ABS_TEXT = " Please don't be selfish."
    UPGRADE_TEXT = "No Upgradation available ❌"
    DOWNLOAD_START = "Trying to download File 📥"
    UPLOAD_START = "Trying to upload 📤"
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 2GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "**File uploaded sucessfully ✅**"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds.\nUploaded in {} seconds."
    NOT_AUTH_USER_TEXT = "You can't use me ❎"
    NOT_AUTH_USER_TEXT_FILE_SIZE = "File size exceeded"
    SAVED_CUSTOM_THUMB_NAIL = "Custom File thumbnail saved. This image will be used in the File."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    SAVED_RECVD_DOC_FILE = "Document Downloaded Successfully."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    HELP_USER = """You can use me to rename Telegram files.
    
💠 Send me any Telegram file.

💠 Send any photo to set as Permanent Thumbnail.

💠 Reply to that message with /rename new name.extension

💠 Use /deletethumbnail to delete current Thumbnail.
"""
    REPLY_TO_DOC_FOR_RENAME_FILE = "Reply to a Telegram media to `/rename New Name.extension` with custom thumbnail support.."
    ABUSIVE_USERS = "You are not allowed to use this bot."
    FREE_USER_LIMIT_Q_SZE = """Cannot Process. Reached limit."""
    IFLONG_FILE_NAME = """File Name limit allowed by Telegram is {alimit} characters.
The given file name has {num} characters.

<b>Reduce your name length!</b>"""

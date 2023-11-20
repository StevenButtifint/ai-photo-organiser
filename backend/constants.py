
STATUS_CODES = {
    200: "OK",
    400: "Invalid folder location given.",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Folder location was not found.",
    500: "Photo classifier model could not be loaded.",
    501: "Photo classifier weights could not be loaded.",
    502: "Classifier class index could not be loaded.",
    503: "Photo classifier could not setup correctly.",
    504: "Photos could not be found.",
    505: "Subfolder location could not be found.",
    506: "Insufficient permissions for subfolder location.",
    507: "Photo could not found and was not moved.",
    900: "A broader exception occurred, check console message."
}

CLASSES_DIR = 'backend\\classes.json'
WORDNET = 'wordnet'

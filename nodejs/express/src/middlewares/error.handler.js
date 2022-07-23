function logErrors(error, request, response, next) {
    console.error(err);
    next(err)
}

function errorHandler(error, request, response, next) {
    response.status(500).json({
        message: error.message,
        stack: error.stack
    })
}

module.exports = {
    logErros,
    errorHandler
}

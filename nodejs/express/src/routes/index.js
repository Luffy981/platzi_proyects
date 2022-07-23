import { productsRouter } from './products.router.js';
import { Express } from 'express';
// import usersRouter from './usersRouter'

function routerApi(app) {
    const router = Express.Router()
    app.use('/api/v1', router)
    router.use('/products', productsRouter)
    // app.use('/users', usersRouter)
}


module.exports = {routerApi}

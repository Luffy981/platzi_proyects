import express from 'express'
import { routerApi } from './routes/index';
import { logErrors, errorHandler } from './middlewares/error.handler'
import cors from 'cors'
const app = express()
const port = 3000

app.use(express.json())
const whitelist = ['http://localhost:8080', 'https://myapp.com']
const options = {
    origin: (origin, callback) = {
        if (whitelist.includes(origin)) {
            callback(null, true)
        } else {
            callback(new Error('no permission'))
        }
    }
}
app.use(cors(options))

app.get('/', (request, response) => {
    response.send('Hola, Soy el rey de los piratas')
})



app.get('/categories/:categoryId/products/:productId', (request, response) => {
    const { categoryId, productId } = request.params;
    response.json({
        categoryId,
        productId,
    })
})

routerApi(app)

// middlewares siempre van despues del routing

app.use(logErrors)
app.use(errorHandler)

app.listen(port, () => {
    console.log('Mi puerto' + port)
})


const jsonServer = require('json-server')
const server = jsonServer.create()
const router = jsonServer.router('./db.json')
const middlewares = jsonServer.defaults()
const port = process.env.PORT || 3000

server.use(jsonServer.rewriter({
    '/api/*': '/$1',
    "/v4/BRLETH/candles\\?*": "/BRLETH",
    "/v1/BRLBTC/candles\\?*": "/BRLBTC"
}));

server.get('/v4/BRLBTC/*', (req, res) => {
    console.log('/v4/BRLBTC/candles?*, error 500')
    res.status(400).send({
        'error': 'error'
    })
})
server.use(middlewares)
server.use(router)





server.listen(port, () => {
  console.log('JSON Server is running on http://localhost:' + port)
})

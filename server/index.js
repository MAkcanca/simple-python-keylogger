const express = require('express')
const bodyParser = require("body-parser")

const app = express()
const router = express.Router()

const port = 5000

app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())

router.post('/check_version',(request,response) => {
    //code to perform particular action.
    //To access POST variable use req.body()methods.
    console.log(request.body);
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})

app.use("/", router)

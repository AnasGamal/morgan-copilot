require('dotenv').config()

const PORT = process.env.PORT
const MONGODB_URI = process.env.MONGODB_URI
const OPENAI_API_KEY= process.env.OPENAI_API_KEY

module.exports = {
  MONGODB_URI,
  PORT,
  OPENAI_API_KEY
}
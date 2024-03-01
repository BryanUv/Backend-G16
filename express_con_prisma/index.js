import express from 'express'
import dotenv from 'dotenv'
// cuando una libreria ha sido desarrollada utilizando Common Js no se puede utilizar la 
// destructuracion en la importacion de EcmaScript pq lanzara error de incompatibilidad
import { PrismaClient } from '@prisma/client'
import Joi from 'joi'

const validacionCategoria = Joi.object({
  nombre: Joi.string().required(),
  habilitado: Joi.boolean().optional()
})

// lee las variables del archivo .env
dotenv.config()
const conexion = new PrismaClient()
const servidor = express()

// nuestro middleware para que acepte json desde el cliente
servidor.use(express.json())

servidor.get('/',(req,res)=>{
  res.json({
    message:'Bienvenido a mi API de minimarket'
  })
})

servidor.post('/categorias', async (req,res)=>{
  const resultado = validacionCategoria.validate(req.body)

  if(resultado.error){
    return res.status(400).json({
      message:'Error al crear la categoria',
      content: resultado.error
    })
  }
  // todas las operaciones con la base de datos 
  const categoriaCreada = await conexion.categoria.create({data: resultado.value}) // {nombre: 'abarrotes', habilitado: false}
  console.log(resultado.value)
  console.log(categoriaCreada)
  await conexion.$disconnect() // asi se cierra la conexion con la base de datos con prisma
  
  res.json({
    message:'Categoria creada exitosamente'
  })
})

// Middleware validara que al ya no encontrar mas rutas, entrar a esa por defecto, si lo ponemos
// antes siempre me iban a devolver este mensaje de error
servidor.use((req,res,next)=>{
  res.status(404).json({
    message:'La ruta que quieres acceder no existe!'
  })
})

servidor.listen(process.env.PORT, () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${process.env.PORT}`)
})
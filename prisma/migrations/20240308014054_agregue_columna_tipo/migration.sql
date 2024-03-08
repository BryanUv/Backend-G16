-- CreateEnum
CREATE TYPE "tipoUsuario" AS ENUM ('ADMIN', 'EMPLEADO', 'CLIENTE');

-- AlterTable
ALTER TABLE "usuarios" ADD COLUMN     "tipo_usuario" "tipoUsuario" NOT NULL DEFAULT 'CLIENTE';

# 🏁 Ejercicio 00 — Dame más...

✨ Objetivo: recrear una salida `ls -l` específica y empaquetarla en `exo.tar`.

---

📁 Directorio de entrega: `ex00/`
📄 Archivos a entregar: `exo.tar`
✅ Funciones autorizadas: Ninguna

---

### 📝 Enunciado

Crea los siguientes archivos y directorios. Haz lo que sea necesario para que, cuando utilices el comando `ls -l` en tu directorio, la salida tenga este aspecto:

```bash
%> ls -l
total XX
drwx--xr-x 2 XX XX XX Jun 1 20:47 test0
-rwx--xr-- 1 XX XX 4 Jun 1 21:46 test1
dr-x---r-- 2 XX XX XX Jun 1 22:45 test2
-r--r--r-- 2 XX XX 1 Jun 1 23:44 test3
-rw-r-xr-- 1 XX XX 2 Jun 1 23:43 test4
-r--r--r-- 2 XX XX 1 Jun 1 23:44 test5
lrwxrwxrwx 1 XX XX 5 Jun 1 22:20 test6 -> test0
%>
```

- Con respecto a las horas, se aceptará que el año que se muestra en la fecha del ejercicio esté desfasado por seis meses o más.
- Una vez hecho esto, ejecuta `tar -cf exo.tar *` para crear el archivo a entregar.

---

### 🔗 Navegación

- ← Anterior: [Índice](../README.md)
- Siguiente: [Ejercicio 01](../ex01/README.md) →

---

¡Manos a la obra! 🛠️
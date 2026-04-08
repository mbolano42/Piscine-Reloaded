# 📐 Ejercicio 23 — ft_point.h

Objetivo: definir `t_point` para que el `main` de ejemplo compile.

---

- 📁 Directorio de entrega: `ex23/`
- 📄 Archivos a entregar: `ft_point.h`
- ✅ Funciones autorizadas: Ninguna

---

### Enunciado

Crea un archivo `ft_point.h` que permita compilar este `main` de ejemplo:

```c
#include "ft_point.h"

void set_point(t_point *point)
{
  point->x = 42;
  point->y = 21;
}

int main(void)
{
  t_point point;
  set_point(&point);
  return (0);
}
```

(La solución típica es declarar `typedef struct s_point { int x; int y; } t_point;` )

---

### Navegación

- ← Anterior: [Ejercicio 22](../ex22/README.md)
- Siguiente: [Ejercicio 24](../ex24/README.md) →

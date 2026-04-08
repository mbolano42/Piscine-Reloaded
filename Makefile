.PHONY: all test clean

all: test

test:
	@bash -c '\
if command -v python3 >/dev/null 2>&1; then \
	echo "python3 encontrado: $$(python3 --version)"; \
else \
	echo "python3 no encontrado."; \
	read -p "Desea instalar python3? [y/N] " yn; \
	case $$yn in \
	  [Yy]* ) \
	    if command -v apt-get >/dev/null 2>&1; then sudo apt-get update && sudo apt-get install -y python3; \
	    elif command -v dnf >/dev/null 2>&1; then sudo dnf install -y python3; \
	    elif command -v yum >/dev/null 2>&1; then sudo yum install -y python3; \
	    elif command -v pacman >/dev/null 2>&1; then sudo pacman -Sy --noconfirm python; \
	    elif command -v zypper >/dev/null 2>&1; then sudo zypper install -y python3; \
	    else echo "No se detectó gestor de paquetes soportado. Instale python3 manualmente."; exit 1; \
	    fi; \
	    ;; \
	  * ) echo "No se instaló python3. Saliendo."; exit 1; ;; \
	esac; \
fi; \
test -x "$(PWD)/.test/test.py" || chmod +x "$(PWD)/.test/test.py"; \
echo "Ejecutando tests..."; \
python3 "$(PWD)/.test/test.py" $(EX) || true; \
echo "Limpiando directorios temporales creados por los tests..."; \
find . -type d \( -name 'build_test' -o -name 'build_ex*' -o -name '__pycache__' \) -exec rm -rf {} + || true; \
echo "Finalizado." '

clean:
	@echo "Limpiando directorios temporales..."; \
	find . -type d \( -name 'build_test' -o -name 'build_ex*' -o -name '__pycache__' \) -exec rm -rf {} + || true; \
	@echo "Limpieza completada."

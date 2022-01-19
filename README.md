![You SHALL NOT PASS!!!](https://i.kym-cdn.com/entries/icons/original/000/002/144/You_Shall_Not_Pass!_0-1_screenshot.jpg)

### Prerequisitos

Instalado python
Instalado pipenv
Instalado geckodriver o algun otro webdriver como chromedirver

### Setup del ambiente de desarrollo

```bash
git clone https://github.com/DPLATA/react_game_app_e2e.git
cd react_game_app_e2e
pipenv shell
pipenv install
```

En caso de tener instalado geckodriver no hay que hacer ninguna modificación. En caso de querer usar chromedriver o algún otro web driver en cada script de prueba se debe  crear la instancia correspondiente del driver a utilizar

Para correr un script:
- elegir el script que se quiere correr

```bash
python test_cases/mi_script.py
```

### Git workflow

Flujo de trabajo para control de versiones del equipo.

| Tipo de rama | Descripción |
| ------------- | ------------- |
| main  | Rama donde se encuentra los scripts de prueba completos  |
| feature  | Toda feature en este caso scripts de prueba sale desde main y hace merge con main.  |

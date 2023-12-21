Как запустить работающий пример:

  1. cd example_works/
  2. docker build -t my-python-server .
  3. docker run -it --rm my-python-server

Как запустить проблемный пример:

  1. cd example_does_not_work/
  2. Удалить volumes/containers с прошлого запуска
  3. docker compose up

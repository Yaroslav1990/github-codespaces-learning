#!/bin/bash
echo "=== Информация о системе в Codespace ==="
echo "1. Версия ядра: $(uname -r)"
echo "2. Количество ядер CPU: $(nproc)"
echo "3. Объем оперативной памяти:"
free -h
echo "4. Внешний IP-адрес: $(curl -s ifconfig.me)"
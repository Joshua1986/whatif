#!/bin/bash

# Source function library.
. /etc/rc.d/init.d/functions

export PREDICTMODEL_PATH="/home/q/www/order_selling_data/"

start() {
    cd "/home/q/www/order_selling_data/"
    nohup /usr/local/bin/gunicorn -w 4 -b 10.90.59.34:10010 run:app 1>nohup.out 2>&1 &
    RETVAL=$?
    return $RETVAL
}

# When stopping ,
stop() {
    pid=`ps -ef |grep -i "10.90.59.34:10010"|grep -v "grep"|awk '{print $2}'`
    if [[ -n $pid ]];then
        sudo kill -9 ${pid}
        if [ $? -eq 0 ];then
            echo "task is killed ..."
        else
            echo "kill task failed "
        fi
    fi
    RETVAL=$?
    return $RETVAL
}

# See how we were called.
case "$1" in
  start)
    start
    ;;
  stop)
    stop
    ;;
  restart)
    stop
    start
    ;;
  *)
    echo $"Usage: $prog {start|stop|restart|status|}"
    RETVAL=2
esac

exit $RETVAL

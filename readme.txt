测试学习Redis
Redis的linux下安装
    1,下载Rides压缩包
    $ wget http://download.redis.io/releases/redis-6.0.3.tar.gz
    2，解压缩
    $ tar xzf redis-6.0.3.tar.gz
    3，进入解压后的目录
    $ cd redis-6.0.3
    4，编译，如果编译失败查看系统是否安装编译器 gc++ gcc
    $ make
Redis环境变量配置
    exprot REDIS_HOME=[安装目录]
    exprot PAHT=$PATH:$REDIS_HOME/src
Redis服务 没有配置文件会选择默认配置
    redis-server [配置文件]
Redis客户端
    redis-cli
    关闭Redis
    redis-cli shutdown
Redis配置文件redis.conf
    daemonize  是否在后台运行
    port 端口
    bind 允许ip访问，不限制则注释
    save 900 1
    save 300 10
    save 60 10000  内存中的数据保存时间
    appendonly no 默认情况下，redis 会在后台异步的把数据库镜像备份到磁盘，但是该备份是非常耗时的，而且备份也不能很频繁。所以redis 提供了另外一种更加高效的数据库备份及灾难恢复方式。开启append only 模式之后，redis 会把所接收到的每一次写操作请求都追加到appendonly.aof 文件中，当redis 重新启动时，会从该文件恢复出之前的状态。但是这样会造成appendonly.aof 文件过大，所以redis 还支持了BGREWRITEAOF 指令，对appendonly.aof 进行重新整理。如果不经常进行数据迁移操作，推荐生产环境下的做法为关闭镜像，开启appendonly.aof，同时可以选择在访问较少的时间每天对appendonly.aof 进行重写一次。
    loglevel notice log 等级分为4 级，debug,verbose, notice, 和warning。生产环境下一般开启notice
    dir ./ 数据库镜像备份的文件rdb/AOF文件放置的路径。
    dbfilename dump.rdb 镜像备份文件的文件名，默认为 dump.rdb
    详细讲解https://blog.csdn.net/neubuffer/article/details/17003909
Redis常用命令
    详细命令http://redisdoc.com/index.html
    set [name] [value]
    mset [name] [value]....
    get [name]
    mget [name]....
    keys *

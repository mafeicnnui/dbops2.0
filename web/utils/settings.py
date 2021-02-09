import os

settings =  {
    "static_path"   : os.path.join(os.path.dirname(__file__), "../../static"),
    "template_path" : os.path.join(os.path.dirname(__file__), "../../templates"),
    "cookie_secret" : "2379874hsdhf0234990sdhsaiuofyasop977djdj",
    "xsrf_cookies"  : False,
    "debug"         : True,
    "db" : {
        "host"     : "10.2.39.17",
        "user"     : "puppet",
        "passwd"   : "Puppet@123",
        "db"       : "puppet2.0",
        "port"     :  23306,
        "charset"  :  "utf8mb4"
    }
}

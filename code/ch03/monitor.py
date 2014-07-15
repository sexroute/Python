10.37.84.114


export http_proxy=http://CHENGSIQIN754:password@10.37.84.114:8080


apt-get-proxy.conf:
Acquire::http::proxy  "http://CHENGSIQIN754:77777Luxe@10.37.84.114:8080";
Acquire::https::proxy  "https://CHENGSIQIN754:77777Luxe@10.37.84.114:8080";
Acquire::ftp::proxy  "ftp://CHENGSIQIN754:77777Luxe@10.37.84.114:8080";

sudo apt-get update -c ~/apt-get-proxy.conf
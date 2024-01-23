# Puppet manifest to install and configure Nginx

exec { 'Update the apt repository':
  command => 'apt update',
  path    => '/usr/bin:/usr/sbin:/bin'
}

package { 'The web server':
  ensure          => installed,
  name            => 'nginx',
  provider        => 'apt',
  install_options => ['-y']
}

file { 'The home page':
  ensure  => file,
  path    => '/var/www/html/index.html',
  mode    => '0744',
  owner   => 'www-data',
  content => "Hello World!\n"
}

file { 'Nginx server config file':
  ensure  => file,
  path    => '/etc/nginx/sites-enabled/default',
  mode    => '0744',
  owner   => 'www-data',
  content =>
"server {
	listen 80 default_server;
	listen [::]:80 default_server;

	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;

	server_name _;

	location / {
		try_files \$uri \$uri/ =404;
	}
}"
}

exec { 'Start the server':
  command => 'service nginx restart',
  path    => '/usr/bin:/usr/sbin:/bin'
}

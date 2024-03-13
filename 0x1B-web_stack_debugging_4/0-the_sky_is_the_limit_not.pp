# Fixes an nginx site that can't handle multiple concurrent requests
exec { 'replace_ulimit':
  command => '/usr/bin/sudo /bin/sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  onlyif  => '/bin/grep -q "ULIMIT=\"-n 15\"" /etc/default/nginx',
  notify  => Exec['restart_nginx'],
}

exec { 'restart_nginx':
  command     => '/usr/bin/sudo /usr/sbin/service nginx restart',
  refreshonly => true,
}

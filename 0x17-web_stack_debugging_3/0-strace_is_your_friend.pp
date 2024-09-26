file { '/etc/apache2/sites-enabled/000-default.conf':
  ensure  => present,
  source  => 'puppet:///modules/apache/000-default.conf',
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  require => Package['apache2'],
}

service { 'apache2':
  ensure     => running,
  enable     => true,
  subscribe  => File['/etc/apache2/sites-enabled/000-default.conf'],
}


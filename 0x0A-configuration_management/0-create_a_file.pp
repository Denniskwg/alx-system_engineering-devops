#create a file in /tmp with mode 0744 owner and group www-data and content I love Puppet
file{ '/tmp/school':
  ensure  => 'file',
  content => 'I love Puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}

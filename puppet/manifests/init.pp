class core {

    exec { "apt-update":
        command => "/usr/bin/sudo apt-get -u update"
    }

    package {
        [ "vim", "git-core", "build-essential" ]:
            ensure => ["installed"],
            require => Exec['apt-update']
    }
}

class python {

    package {
        [ "python", "python-setuptools", "python-dev", "python-pip" ]:
            ensure => ["installed"],
            require => Exec['apt-update']
    }

    exec {
        "virtualenv":
        command => "/usr/bin/sudo pip install virtualenv",
        require => Package["python-dev", "python-pip"]
    }
}

class flask {

    exec {
        "fabric":
            command => "/usr/bin/sudo pip install Flask",
            require => Package["python-pip"],
    }

    exec {
        "flask-sqlalchemy":
            command => "/usr/bin/sudo pip install Flask-SQLAlchemy",
            require => Package["python-pip"],
    }
 
    exec {
        "flask-script":
            command => "/usr/bin/sudo pip install Flask-Script",
            require => Package["python-pip"],
    }

    exec {
        "flask-wtforms":
            command => "/usr/bin/sudo pip install Flask-WTF",
            require => Package["python-pip"],
    }
}

class grako {

    exec {
        "grako":
            command => "/usr/bin/sudo pip install grako",
            require => Package["python-pip"],
    }
}

include core
include python
include flask
include grako


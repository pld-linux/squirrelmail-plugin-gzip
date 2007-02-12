%define		_plugin	gzip
%define		mversion	1.1.1
Summary:	Plugin for compressed tranfer support
Summary(pl.UTF-8):   Wtyczka pozwalająca kompresować transmisję
Name:		squirrelmail-plugin-%{_plugin}
Version:	2.02
Release:	2
License:	GPL
Group:		Applications/Mail
Source0:	http://www.squirrelmail.org/plugins/%{_plugin}-%{version}-%{mversion}.tar.gz
# Source0-md5:	2df7370e0dbdf3e48e888cef094ead8b
URL:		http://www.squirrelmail.org/plugin_view.php?id=19
Requires:	php(zlib)
Requires:	squirrelmail >= 1.4.6-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_datadir}/squirrelmail/plugins/%{_plugin}
%define		_sysconfdir	/etc/webapps/squirrelmail

%description
This plugin allows SquirrelMail to compress its output to the browser,
saving precious bandwidth.

%description -l pl.UTF-8
Wtyczka pozwalająca na kompresję transmisji między Wiewiórczą Pocztą i
przeglądarką użytkownika. Oszczędza cenną przepustowość łącza.

%prep
%setup -q -n %{_plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir} $RPM_BUILD_ROOT%{_sysconfdir}

install *.php $RPM_BUILD_ROOT%{_plugindir}
mv locale $RPM_BUILD_ROOT%{_plugindir}
mv config.php.sample $RPM_BUILD_ROOT%{_sysconfdir}/%{_plugin}_config.php
ln -s %{_sysconfdir}/%{_plugin}_config.php $RPM_BUILD_ROOT%{_plugindir}/config.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL README
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{_plugin}_config.php
%dir %{_plugindir}
%{_plugindir}/*.php
%dir %{_plugindir}/locale
%lang(el) %{_plugindir}/locale/el_GR

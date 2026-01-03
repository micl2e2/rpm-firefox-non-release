%global             application_name_esr firefox-esr
%global             application_name_dev firefox-dev
%global             application_name_nightly firefox-nightly
%global             full_name_esr firefox-esr-edition
%global             full_name_dev firefox-dev-edition
%global             full_name_nightly firefox-nightly-edition
%global             internal_name_esr firefox-esr
%global             internal_name_dev firefox-dev
%global             internal_name_nightly firefox-nightly
%global             debug_package %{nil}
%global             version_esr 140.6.0esr
%global             version_dev 147.0b9
%global             version_nightly 148.0a1
%global             local_sources_dir firefox-non-release-local-sources

Name:               firefox-non-release
Version:            1.0
Release:            6%{?dist}
Summary:            Firefox non-release editions collection, such as ESR, Developer, Nightly, etc.

License:            MPLv1.1 or GPLv2+ or LGPLv2+
URL:                https://www.mozilla.org/en-US/firefox/
Source0:            firefox-non-release-local-sources.tar 
Source8:            https://download-installer.cdn.mozilla.net/pub/firefox/releases/%{version_esr}/linux-x86_64/en-US/firefox-%{version_esr}.tar.xz
Source9:            https://download-installer.cdn.mozilla.net/pub/devedition/releases/%{version_dev}/linux-x86_64/en-US/firefox-%{version_dev}.tar.xz
Source10:            https://download-installer.cdn.mozilla.net/pub/firefox/nightly/latest-mozilla-central/firefox-%{version_nightly}.en-US.linux-x86_64.tar.xz

ExclusiveArch:      x86_64

Recommends:         (gnome-browser-connector if gnome-shell)

BuildRequires:      chrpath

Requires(post):     gtk-update-icon-cache

%description
This is a pre-beta release of Mozilla Firefox intended for Web developers and
enthusiasts who want early access to new features. It receives new updates
(almost) daily, adding and refining support for the very latest Web standards
that won't make it into the stable release of Firefox for some months. It also
comes with some addons for Web development enabled by default.

You may actually find that Developer Edition works just fine for normal everyday
use: Some users set it as their default Web browser. You can sign in to your
normal Firefox account and sync your preferences, extensions, and bookmarks,
etc. Or you can keep the Firefox versions separate, and use different profiles,
even different browser UI themes. Firefox Developer Edition can install
alongside the stable release of Firefox, making it easy to switch back and forth
between the two versions.

That being said, a lot of the technology here is still experimental, and there
will very likely be some bugs, so just remember that by using Developer Edition,
you're helping Mozilla make Firefox the best Web browser they can. And have fun!

Bugs related to Firefox Developer Edition should be reported directly to Mozilla: 
<https://bugzilla.mozilla.org/>

Bugs related to this package should be reported at this GitHub project:
<https://github.com/the4runner/firefox-dev/issues/>

%prep
%setup -q -c

%install
%__rm -rf %{buildroot}

%__install -d %{buildroot}{/opt/firefox-non-release/%{application_name_esr},/opt/firefox-non-release/%{application_name_dev},/opt/firefox-non-release/%{application_name_nightly},%{_bindir},%{_datadir}/applications,%{_datadir}/icons/hicolor/128x128/apps,%{_datadir}/icons/hicolor/64x64/apps,%{_datadir}/icons/hicolor/48x48/apps,%{_datadir}/icons/hicolor/32x32/apps,%{_datadir}/icons/hicolor/16x16/apps}

tar -xf %{SOURCE8}
mv firefox %{application_name_esr}

tar -xf %{SOURCE9}
mv firefox %{application_name_dev}

tar -xf %{SOURCE10}
mv firefox %{application_name_nightly}

%__cp -r %{application_name_esr} %{buildroot}/opt/firefox-non-release
%__cp -r %{application_name_dev} %{buildroot}/opt/firefox-non-release
%__cp -r %{application_name_nightly} %{buildroot}/opt/firefox-non-release

# %__cp -r * %{buildroot}/opt/%{application_name_nightly}
# #ERROR   0002: file '/opt/firefox-dev/libonnxruntime.so' contains an invalid runpath '$' in [$]
chrpath --delete %{buildroot}/opt/firefox-non-release/%{application_name_esr}/libonnxruntime.so || :
chrpath --delete %{buildroot}/opt/firefox-non-release/%{application_name_dev}/libonnxruntime.so || :
chrpath --delete %{buildroot}/opt/firefox-non-release/%{application_name_nightly}/libonnxruntime.so || :

%__install -D -m 0644 %{local_sources_dir}/%{application_name_esr}.desktop -t %{buildroot}%{_datadir}/applications
%__install -D -m 0644 %{local_sources_dir}/%{application_name_dev}.desktop -t %{buildroot}%{_datadir}/applications
%__install -D -m 0644 %{local_sources_dir}/%{application_name_nightly}.desktop -t %{buildroot}%{_datadir}/applications

%__install -D -m 0444 %{local_sources_dir}/policies.json -t %{buildroot}/opt/firefox-non-release/%{application_name_esr}/distribution
%__install -D -m 0444 %{local_sources_dir}/policies.json -t %{buildroot}/opt/firefox-non-release/%{application_name_dev}/distribution
%__install -D -m 0444 %{local_sources_dir}/policies.json -t %{buildroot}/opt/firefox-non-release/%{application_name_nightly}/distribution

%__install -D -m 0755 %{local_sources_dir}/%{application_name_esr} -t %{buildroot}%{_bindir}
%__install -D -m 0755 %{local_sources_dir}/%{application_name_dev} -t %{buildroot}%{_bindir}
%__install -D -m 0755 %{local_sources_dir}/%{application_name_nightly} -t %{buildroot}%{_bindir}

%__ln_s ../../../../../../opt/firefox-non-release/%{application_name_esr}/browser/chrome/icons/default/default128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{full_name_esr}.png
%__ln_s ../../../../../../opt/firefox-non-release/%{application_name_esr}/browser/chrome/icons/default/default64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{full_name_esr}.png
%__ln_s ../../../../../../opt/firefox-non-release/%{application_name_esr}/browser/chrome/icons/default/default48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{full_name_esr}.png
%__ln_s ../../../../../../opt/firefox-non-release/%{application_name_esr}/browser/chrome/icons/default/default32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{full_name_esr}.png
%__ln_s ../../../../../../opt/firefox-non-release/%{application_name_esr}/browser/chrome/icons/default/default16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{full_name_esr}.png
#
%__ln_s ../../../../../../opt/firefox-non-release/%{application_name_dev}/browser/chrome/icons/default/default128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{full_name_dev}.png
%__ln_s ../../../../../../opt/firefox-non-release/%{application_name_dev}/browser/chrome/icons/default/default64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{full_name_dev}.png
%__ln_s ../../../../../../opt/firefox-non-release/%{application_name_dev}/browser/chrome/icons/default/default48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{full_name_dev}.png
%__ln_s ../../../../../../opt/firefox-non-release/%{application_name_dev}/browser/chrome/icons/default/default32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{full_name_dev}.png
%__ln_s ../../../../../../opt/firefox-non-release/%{application_name_dev}/browser/chrome/icons/default/default16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{full_name_dev}.png
#
%__ln_s ../../../../../../opt/firefox-non-release/%{application_name_nightly}/browser/chrome/icons/default/default128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{full_name_nightly}.png
%__ln_s ../../../../../../opt/firefox-non-release/%{application_name_nightly}/browser/chrome/icons/default/default64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{full_name_nightly}.png
%__ln_s ../../../../../../opt/firefox-non-release/%{application_name_nightly}/browser/chrome/icons/default/default48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{full_name_nightly}.png
%__ln_s ../../../../../../opt/firefox-non-release/%{application_name_nightly}/browser/chrome/icons/default/default32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{full_name_nightly}.png
%__ln_s ../../../../../../opt/firefox-non-release/%{application_name_nightly}/browser/chrome/icons/default/default16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{full_name_nightly}.png

%post
gtk-update-icon-cache -ftq %{_datadir}/icons/hicolor

%files
/opt/firefox-non-release/
#
%{_datadir}/applications/%{internal_name_esr}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{full_name_esr}.png
%{_datadir}/icons/hicolor/64x64/apps/%{full_name_esr}.png
%{_datadir}/icons/hicolor/48x48/apps/%{full_name_esr}.png
%{_datadir}/icons/hicolor/32x32/apps/%{full_name_esr}.png
%{_datadir}/icons/hicolor/16x16/apps/%{full_name_esr}.png
%{_bindir}/%{application_name_esr}
#
%{_datadir}/applications/%{internal_name_dev}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{full_name_dev}.png
%{_datadir}/icons/hicolor/64x64/apps/%{full_name_dev}.png
%{_datadir}/icons/hicolor/48x48/apps/%{full_name_dev}.png
%{_datadir}/icons/hicolor/32x32/apps/%{full_name_dev}.png
%{_datadir}/icons/hicolor/16x16/apps/%{full_name_dev}.png
%{_bindir}/%{application_name_dev}
#
%{_datadir}/applications/%{internal_name_nightly}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{full_name_nightly}.png
%{_datadir}/icons/hicolor/64x64/apps/%{full_name_nightly}.png
%{_datadir}/icons/hicolor/48x48/apps/%{full_name_nightly}.png
%{_datadir}/icons/hicolor/32x32/apps/%{full_name_nightly}.png
%{_datadir}/icons/hicolor/16x16/apps/%{full_name_nightly}.png
%{_bindir}/%{application_name_nightly}

%changelog
# * Wed Jul 10 2024 AnjaloHettiarachchi <24694418+AnjaloHettiarachchi@users.noreply.github.com> - 129.0b1
# - firefox-developer-edition.spec: Add global declaration to disable debuginfo

# * Sat Sep 23 2023 Namelesswonder <Namelesswonder@users.noreply.github.com> - 118.0b9-3
# - firefox-developer-edition.spec: Add weak dependency for each DE browser integration

# * Tue Sep 12 2023 Namelesswonder <Namelesswonder@users.noreply.github.com> - 118.0b7-2
# - firefox-developer-edition.spec: Trim changelog to resolve date warnings and bump release

V_ESR=$(curl -s https://download-installer.cdn.mozilla.net/pub/firefox/releases/ | grep esr/ | sed -E 's/.*">([0-9.]+esr)\/<.*/\1/' | sed '/^[^1-9]/d' | sort -g | tail -1)

V_DEV=$(curl -s https://download-installer.cdn.mozilla.net/pub/devedition/releases/ | sed -E 's/.*">([0-9.]+b?[1-9]+)\/<.*/\1/' | sed '/^[^1-9]/d' | sort -g | tail -1)

V_NIGHTLY=$(curl -s https://download-installer.cdn.mozilla.net/pub/firefox/nightly/latest-mozilla-central/ | grep '>firefox.*x86_64.tar.xz<' | sed -E 's/.*firefox-([0-9.]+a[1-9]+)\..*/\1/')

sed -e "s/%global             version_esr .*/%global             version_esr $V_ESR/" -e "s/%global             version_dev .*/%global             version_dev $V_DEV/" -e "s/%global             version_nightly .*/%global             version_nightly $V_NIGHTLY/" -i firefox-non-release.spec

 

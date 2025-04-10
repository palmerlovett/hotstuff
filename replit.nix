
{pkgs}: {
  deps = [
    pkgs.playwright-driver
    pkgs.chromium
    pkgs.xorg.libX11
    pkgs.xorg.libXcomposite
    pkgs.xorg.libXdamage
    pkgs.xorg.libXext
    pkgs.xorg.libXfixes
    pkgs.xorg.libXrandr
    pkgs.alsaLib
    pkgs.atk
    pkgs.cairo
    pkgs.cups
    pkgs.dbus
    pkgs.expat
    pkgs.fontconfig.lib
    pkgs.freetype
    pkgs.gdk-pixbuf
    pkgs.glib
    pkgs.gtk3
    pkgs.libdrm
    pkgs.libuuid
    pkgs.nspr
    pkgs.nss
    pkgs.pango
    pkgs.libnotify
    pkgs.libxkbcommon
    pkgs.mesa
    pkgs.gnome2.GConf
    pkgs.gitFull
  ];
}

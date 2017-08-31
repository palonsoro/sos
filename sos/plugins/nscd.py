# Copyright (C) 2007 Shijoe George <spanjikk@redhat.com>

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from sos.plugins import Plugin, RedHatPlugin, DebianPlugin, UbuntuPlugin


class Nscd(Plugin, RedHatPlugin, DebianPlugin, UbuntuPlugin):
    """Name service caching daemon
    """

    plugin_name = 'nscd'
    profiles = ('services', 'identity', 'system')

    files = ('/etc/nscd.conf',)
    packages = ('nscd',)

    def setup(self):
        self.add_copy_spec("/etc/nscd.conf")

        self.limit = (None if self.get_option("all_logs")
                      else self.get_option("log_size"))
        opt = self.file_grep(r"^\s*logfile", "/etc/nscd.conf")
        if (len(opt) > 0):
            for o in opt:
                f = o.split()
                self.add_copy_spec(f[1], sizelimit=self.limit)

# vim: set et ts=4 sw=4 :

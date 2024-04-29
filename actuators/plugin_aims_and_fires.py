# Copyright (c) 2024 Martín Abente Lahaye.
#
# This file is part of Gameeky
# (see gameeky.tchx84.dev).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from gameeky.plugins import Actuator as Plugin
from gameeky.common.definitions import Action, Direction


class Actuator(Plugin):
    interactable = False
    activatable = False

    def tick(self) -> None:
        if self.entity.held is None:
            return

        if self.entity.target is None:
            return

        if self.entity.target.blocked:
            return

        if not self.entity.inline_with(self.entity.target):
            return

        delta_x = self.entity.target.position.x - self.entity.position.x
        delta_y = self.entity.target.position.y - self.entity.position.y

        if delta_x > 0:
            direction = Direction.EAST
        elif delta_x < 0:
            direction = Direction.WEST
        elif delta_y > 0:
            direction = Direction.SOUTH
        elif delta_y < 0:
            direction = Direction.NORTH

        self.entity.direction = direction
        self.entity.perform(Action.USE)

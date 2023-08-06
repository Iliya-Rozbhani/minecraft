from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

block1_block = load_texture('image/block1_block.png')
block2_block = load_texture('image/block2_block.png')
block3_block = load_texture('image/block3_block.png')
block4_block = load_texture('image/block4_block.png')
block5_block = load_texture('image/block5_block.png')
block6_block = load_texture('image/block6_block.png')
block7_block = load_texture('image/block7_block.png')
sky_texture  = load_texture('image/skybox.png')
arm_texture  = load_texture('image/arm_texture.png')
punch_sound  = Audio('image/punch_sound',loop = False, autoplay = False)
block_pick = 1

window.fps_counter.enabled = False
window.exit_button.visible = False

def update():
	global block_pick

	if held_keys['left mouse'] or held_keys['right mouse']:
		hand.active()
	else:
		hand.passive()

	if held_keys['1']: block_pick = 1
	if held_keys['2']: block_pick = 2
	if held_keys['3']: block_pick = 3
	if held_keys['4']: block_pick = 4
	if held_keys['5']: block_pick = 5
	if held_keys['6']: block_pick = 6	
	if held_keys['7']: block_pick = 7
	if held_keys['8']: block_pick = 8
	if held_keys['9']: block_pick = 9
	if held_keys['-']: exit()

class Voxel(Button):
	def __init__(self, position = (0,0,0), texture = block1_block):
		super().__init__(
			parent = scene,
			position = position,
			model = 'image/block',
			origin_y = 0.5,
			texture = texture,
			color = color.color(0,0,random.uniform(0.9,1)),
			scale = 0.5)

	def input(self,key):
		if self.hovered:
			if key == 'left mouse down':
				punch_sound.play()
				if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = block1_block)
				elif block_pick == 2: voxel = Voxel(position = self.position + mouse.normal, texture = block2_block)
				elif block_pick == 3: voxel = Voxel(position = self.position + mouse.normal, texture = block3_block)
				elif block_pick == 4: voxel = Voxel(position = self.position + mouse.normal, texture = block4_block)
				elif block_pick == 5: voxel = Voxel(position = self.position + mouse.normal, texture = block5_block)
				elif block_pick == 6: voxel = Voxel(position = self.position + mouse.normal, texture = block6_block)
				elif block_pick == 7: voxel = Voxel(position = self.position + mouse.normal, texture = block7_block)

			if key == 'right mouse down':
				punch_sound.play()
				destroy(self)

class Sky(Entity):
	def __init__(self):
		super().__init__(
			parent = scene,
			model = 'sphere',
			texture = sky_texture,
			scale = 150,
			double_sided = True)

class Hand(Entity):
	def __init__(self):
		super().__init__(
			parent = camera.ui,
			model = 'image/arm',
			texture = arm_texture,
			scale = 0.2,
			rotation = Vec3(150,-10,0),
			position = Vec2(0.4,-0.6))

	def active(self):
		self.position = Vec2(0.3,-0.5)

	def passive(self):
		self.position = Vec2(0.4,-0.6)

for z in range(50):
	for x in range(50):
		voxel = Voxel(position = (x,0,z))

player = FirstPersonController()
sky = Sky()
hand = Hand()

app.run()
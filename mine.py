import selen_scrap as scp


waifu_type = "cosmos"
n_images = 50
width = 500
height = 500
path = "results"
name_to_save = "cosmos_proof"

scp.pages_loop(waifu_type, n_images, width, height, path, name_to_save)

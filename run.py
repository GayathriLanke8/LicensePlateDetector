from module import *


def run():
    obj_model, ocr_model = load_object("license_plate_detector.pt"), load_ocr()
    for file_name in os.listdir("images"):
        if file_name.lower().endswith((".jpg", ".png", ".jpeg")):
            img_path = os.path.join("images", file_name)

            img = load_image(img_path)
            coords = get_coordinates(img, obj_model)
            crop = cropped_image(img, coords)

            state_name = extract_text(crop, ocr_model, "data.json")

            print(f"The car belongs to {state_name} state")

run()



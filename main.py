import cv2
import numpy as np

def load_and_split_by_rows(input_image_path, output_path1, output_path2):
    # Load image
    image = cv2.imread(input_image_path)

    # Split image
    image1 = image[::2, :, :]
    image2 = image[1::2, :, :]

    # Save the splitted images
    cv2.imwrite(output_path1, image1)
    cv2.imwrite(output_path2, image2)

def load_and_split_by_columns(input_image_path1, input_image_path2, output_path3):
    # Load images
    image1 = cv2.imread(input_image_path1)
    image2 = cv2.imread(input_image_path2)

    # Ensure both images have the same height
    min_height = min(image1.shape[0], image2.shape[0])
    print(min_height)
    image1 = image1[:min_height, :, :]
    image2 = image2[:min_height, :, :]

    # Combine images along columns using NumPy
    result_image1 = np.concatenate((image1[:, ::2, :], image2[:, ::2, :]), axis=1)

    # Save the final splitted images
    cv2.imwrite(output_path3, result_image1)


example = "example.jpg"

# Step 1: Load image and split by rows
load_and_split_by_rows(example, "output_image1.jpg", "output_image2.jpg")

# Step 2: Load splitted images and split by columns
load_and_split_by_columns("output_image1.jpg", "output_image2.jpg", "output_image3.jpg")

image0 = cv2.imread(example)
image1 = cv2.imread("output_image1.jpg")
image2 = cv2.imread("output_image2.jpg")
image3 = cv2.imread("output_image3.jpg")


result_image = np.concatenate((image0, image1, image2, image3), axis=0)

# Save the final image using OpenCV
cv2.imwrite("final_result.jpg", result_image)

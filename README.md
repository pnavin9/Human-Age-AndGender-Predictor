# Human Age Predictor

This application is designed to predict the age and gender of a person from an input image. It utilizes the ResNet-101V2 model, which has been fine-tuned on a facial dataset, to recognize and analyze the input image.

## Installation

1. Clone the repository to your local machine:
   ```
   git clone <repository_url>
   ```

2. Navigate to the project directory:
   ```
   cd human-age-predictor
   ```

3. Install the required dependencies using pip:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the application by running the following command:
   ```
   python app.py
   ```

2. Open your web browser and visit [127.0.0.1:5000/predict](http://127.0.0.1:5000/predict) or [localhost:5000/predict](http://localhost:5000/predict).

3. On the web page, you will find an option to upload an image file. Choose an image containing a person's face.

4. Click the "Predict" button to initiate the prediction process.

5. The application will analyze the image using the pre-trained ResNet-101V2 model and provide an estimated age of the person in the image.

## Demo




https://github.com/pnavin9/Human-Age-Predictor/assets/106406724/22d6fdca-5377-4713-9612-89420a7f5a89



## Performance

The root mean square error (RMSE) of the age predictions made by the model is approximately 8.05. Please note that this value may vary based on the specific dataset and model configuration used during training.

Feel free to explore the application and experiment with different images to predict the age of individuals accurately.

## License

[MIT License](LICENSE)

Please refer to the license file for more information regarding the usage and distribution of this application.

## Contact

For any questions or inquiries, please contact patwarinavin9@gmail.com.

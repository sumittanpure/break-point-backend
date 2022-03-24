from loguru import logger
import firebase_admin


firebase_config = {
    "type": "service_account",
    "project_id": "breakpoint-3d4ff",
    "private_key_id": "6febff3cbba00b3e5a4b630ec56382f3cbd487b7",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCwtXOLXkCx8Cpj\nJGx0Uago6ikZSw0eO8tzcFyc/cl75uLPVBSo3miH3po4m5lE2/hurpN82OoHs1e9\ni1Lry8a8GDxaZvgNcDaMIPiX0FZuCEovMy92cIjFudnVB6yBoK/bovQ/IliEWUEr\nxuiEtQ7ctEqXm7zsGQLOqc4N15kHSCXGmmb0u8hE2cPlfTnywuBoojmrlm4pFTPu\nQJU81K762B1Zw0rEJRi27/bITUi232n+HMSXlCoUqMipnGAGGQDN1QCBC4UfBElI\nwaKHmbBmy2lwm43p1uenPkOEXd9eECJxwP0cdi303/YeZKpUbxqD7WE3IqHOY/Xe\n18ITEQehAgMBAAECggEAAvcrQbxVXJxvBwE+UAjAyDL/I+gGXSqxZDYPWn5zKlZP\nxHKg8sviDYmsT+U4l2xo876P8L6ZKtjqe4lXh70rOs6IphcSnvMc+ea3FUvPRNh0\nb5dYersyaGhmjJ8s2Mi6usu2H/XHw4IrSFH1u/29NUdR9c+3cMTjWawwLjufMKfm\nQjCO18r07GQWHn4Tq9bSPhai/qzn1ELHRXFTVugR/eCReb1ddGMpbF9jCxB4W1g+\nfJ4QAk6McFIsBnah9Mf8YjIN44XreGZRxkvtdBW+1daOAThIDw5vcBTigOc+LHXM\n2/gUinVvXUgE69LTh2l4uSE201ew48C+1iPHTLH5wwKBgQD19h7nCqykrUhC9UWE\nyxav3BqDtLstiq50JCjdfz/kuYo7GlBzKq2IkaMaOxt4R6tbgmE8SsmmWQArtEYu\nGpRixVLv5j5nNoyhPje/xDe8A1Kichij/1l9mRiyQ6ErumOqZmOalRoP+pZLvMB1\n28Z+KdF7L0IESR7zZUwY6jfogwKBgQC368IisFeEQ0RrClGpTbslIDUPi0QIheXA\noVYwBlcro7+zPFfpsjqpgkFl7nx4w8n+sA3I2Cnj2wRbe1UWtPLenxTDYxljCrGS\n3x7Bvy92t1Soeih1nHoeP5KO27MaC+E7Tus2aULxPKb0yR/WEccISpsnCTFKg9dv\nbzMb1wuuCwKBgQCa+h9ymKk7geu8NOs+xvBekqMqRaCDC5TsnTQajGln5viQUP5L\n8qIxIQLSLlgaq53vJPG7mawBYqbW4tothpXkvkyJ2FuNkTN/DcL2094CW12f+aBJ\nBUYP+30yJabR9LmDzswHxNcNJmm5Aw+Js5cYO6VApwBDzwbvee4+7KWZnQKBgHeX\n5uHVluLbNsb/q8ASWmm2uqoD3dZI8u/COR/7T32B+epbh7LfgQOuPkZAwFFqxpNE\n+YGrBfoy9W9jEB42xWJ7QO4YJ27eij89tGs5nWxto6/11w87E7FNl0grlheOuANv\nusTjx3LEBLBRg9EYODqtAJxufs28Uz8TqMEmoWKnAoGAWcAE6BwNOxZKO/37ehhS\nzY4ekuiR0J3PEhTgcPdUXf0ocyaFmQnWfK+wd1TBTiMJc7cB0TUOzoZqk+j7DZ7+\nSzaK7fdt5ztlrQZdgByDQUT9vTvCPbYfRPQXSgGTMjrxkyH/WBUCkloreX51FSLT\nR1PQAkF1KRaDof1hXJiA7eY=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-7h6c2@breakpoint-3d4ff.iam.gserviceaccount.com",
    "client_id": "110957270247292225628",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-7h6c2%40breakpoint-3d4ff.iam.gserviceaccount.com"
}


cred = firebase_admin.credentials.Certificate(firebase_config)


try:
    # firebase_auth = firebase_admin.initialize(cred)
    firebase_app = firebase_admin.initialize_app(cred)
except Exception as e:
    logger.debug(f"Error Initialising Firebase Connection: {e}")

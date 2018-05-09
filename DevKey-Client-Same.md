No, **Client id** and **Developer key** both are different.

**Proof &raquo;** The MATLAB code available under the **Functions** tab of this webpage [MATLAB - Upload video to YouTube](https://in.mathworks.com/matlabcentral/fileexchange/19258-upload-a-video-to-youtube™) uses **Client ID** and **Developer key** both.

Below is the fragment of that code which  shows it:

	% Define needed variables.
    username = getPrefOrPrompt('Username');
    password = getPrefOrPrompt('Password');
    developerKey = 'AI39si7J7QPwNZriOcSa6z2wpbYbN2pFgI9Xdvv4EYSq84Ss3EclSWorSJ4Dtqr2gLyXPSGsDlGyldEsGa9pB_UwNmaXYiCVXA';
    clientid = 'ytapi-MatthewSimoneau-YouTubeUploadfro-ge7j8nsn-0';

	% Upload the file.
    service = YouTubeService(clientid, developerKey);

If you will visit [Google Cloud platform - API credentials page](https://console.cloud.google.com/apis/credentials) and select your application. You will see 3 things **Client ID**, **Client secret** and **Creation date** as the below image shows.



So in my opinion, **Client secret** is your **Developer key** and **Client ID** is your **Client id**. Once try it and comment if really it is.

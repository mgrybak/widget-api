<?php


$curl = curl_init();

if(isset($_POST['url']))
{
    $url = $_POST['url'];
}

curl_setopt_array($curl, array(
  #CURLOPT_URL => "https://platform-api.findthebest.com/API/v1/publisher/exists?name=rybak",	
  CURLOPT_URL => $url,
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "GET",
  CURLOPT_HTTPHEADER => array(
    "token: redacted"
  ),
));

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}

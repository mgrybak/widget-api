<?php


$curl = curl_init();

if(isset($_POST['org_name']))
{
    $org_name = $_POST['org_name'];
}
if(isset($_POST['color']))
{
    $color = $_POST['color'];
}
if(isset($_POST['font']))
{
    $font = $_POST['font'];
}
if(isset($_POST['theme']))
{
    $theme = $_POST['theme'];
}

$theme_data = array("theme_combo" => $org_name,
              "link_color" => $color,
              "font" => $font,
              "chart_theme" => $theme);

$theme_data_string = json_encode($theme_data);

$useragent="Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.1) Gecko/20061204 Firefox/2.0.0.1"; 

curl_setopt_array($curl, array(
  CURLOPT_URL => "https://platform-api.findthebest.com/API/v1/app/12228/import",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => array("data" => "[" . $theme_data_string . "]"),
  CURLOPT_USERAGENT => $useragent,
  CURLOPT_HTTPHEADER => array(
    "content-type: multipart/form-data",
    "token: 021db13568dc101bf462a67884dbf685"
  )
));

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}

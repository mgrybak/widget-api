<?php


$curl = curl_init();

if(isset($_POST['org_name']))
{
    $org_name = $_POST['org_name'];
}
if(isset($_POST['domain']))
{
    $domain = $_POST['domain'];
}
if(isset($_POST['email']))
{
    $email = $_POST['email'];
}
if(isset($_POST['color']))
{
    $color = $_POST['color'];
}
if(isset($_POST['package_option']))
{
    $package_option = $_POST['package_option'];
}
if(isset($_POST['title']))
{
    $title = $_POST['title'];
}
if(isset($_POST['native_integration']))
{
    $native_integration = $_POST['native_integration'];
}
if(isset($_POST['footer']))
{
    $footer = $_POST['footer'];
}
if(isset($_POST['sources']))
{
    $sources = $_POST['sources'];
}
if(isset($_POST['share']))
{
    $share = $_POST['share'];
}

$data = array("organization_name" => $org_name,
              "root_domain" => $domain,
              "email" => $email,
              "color" => $color,
              "package" => $package_option,
              "title" => $title,
              "native_integration" => $native_integration,
              "footer" => $footer,
              "sources" => $sources,
              "share" => $share);

$data_string = json_encode($data);

$useragent="Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.1) Gecko/20061204 Firefox/2.0.0.1"; 

curl_setopt_array($curl, array(
  CURLOPT_URL => "https://platform-api.findthebest.com/API/v1/app/12228/import",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => array("data" => "[" . $data_string . "]"),
  CURLOPT_USERAGENT => $useragent,
  CURLOPT_HTTPHEADER => array(
    "content-type: multipart/form-data",
    "token: 4cfb5a9ab0b0492f0d5aada5b4ac7300"
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
<!DOCTYPE html>
<html lang="en">
<head>
   <?php header("Access-Control-Allow-Origin: http://kabyr.com");
   header("Access-Control-Allow-Methods: GET, POST") ?>
  <title>Graphiq API</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  <script src="api_form.js"></script>
</head>
<body>
<div class="container">  
  <div class="jumbotron">
    <h1>Graphiq API</h1> 
    <p>The Graphiq API is a turnkey solution for real estate professional seeking to increase engagement on their sites. Get started with the Graphiq API by selecting from the options below.</p> 
  </div>
</div>

<div id="register-name" class="container">
  <div class="well well-md">
    <h4><b>Start by entering the name of the organization you wish to register with the Graphiq API</b></h4>
      <div class="container">
        <div class="col-sm-6">
        <form>
          <div class="form-group">
            <label for="usr">Organization Name</label>
            <input type="text" class="form-control" id="usr" placeholder="Graphiq">
          </div>
          <div class="form-group">
            <label for="url">Domain URL</label>
            <input type="text" class="form-control" id="url" placeholder="www.graphiq.com">
          </div>
        </form>
      </div>
    </div>
    <div class="container row">
        <button id="check-availability" type="button" class="btn btn-primary">Check Name Availability</button>
      </div>
  </div>
</div>

<div id="package" class="container">
  <div class="well well-md">
    <h4><b>Specify your visualization package</b></h4>
    <div class="container">
      <form class="form-horizontal">
        <div class="radio">
          <label><input type="radio" name="optradio">Location</label>
        </div>
        <div class="radio">
          <label><input type="radio" name="optradio">Property</label>
        </div>
        <div class="radio">
          <label><input type="radio" name="optradio">Both (Property & Location)</label>
        </div>
      </form>
    </div>
  </div>
</div>

<div id="prefs" class="container">
  <div class="well well-md">
    <h4><b>Specify your customization preferences</b></h4>
    <div class="container">
      <form class="form-horizontal">
        <div class="checkbox">
          <label><input type="checkbox" value="">Title</label>
        </div>
        <div class="checkbox">
          <label><input type="checkbox" value="">Native Background Integration</label>
        </div>
        <div class="checkbox disabled">
          <label><input type="checkbox" value="">Graphiq Footer Icon</label>
        </div>
        <div class="checkbox disabled">
          <label><input type="checkbox" value="">Data Source Citation</label>
        </div>
        <div class="checkbox disabled">
          <label><input type="checkbox" value="">Share Button</label>
        </div>
        <div class="form-group col-md-2" style="margin-top:10px">
          <label for="hex">Color</label>
          <input type="text" class="form-control" id="hex" placeholder="#3d3d3d">
        </div>
      </form>
    </div>
  </div>
</div>

<div id="submit" class="container">
  <div class="well well-md">
    <h4><b>Review</b></h4> 
    <p>Review your preferences and submit the form</p>
    <button type="button" class="btn btn-warning btn-block">Submit</button>
  </div>
</div>

</body>
</html>

  
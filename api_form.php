<!DOCTYPE html>
<html lang="en">
<head>
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

<form action="#">
  <div id="register-name" class="container">
    <div class="well well-md">
      <h4><b>Start by entering the name of the organization you wish to register with the Graphiq API</b></h4>
      <div class="row">
        <div class="form-group col-md-6">
          <label for="usr">Organization Name (25 character max.)</label>
          <input type="text" class="form-control" id="usr" placeholder="Graphiq" value="">
          <span class="" for="usr" aria-hidden="true"></span>
        </div>
      </div>
      <div class="row">
        <div class="form-group col-md-6">
          <label for="url">Domain URL</label>
          <input type="text" class="form-control" id="url" placeholder="www.graphiq.com" value="">
          <span class="" for="url" aria-hidden="true"></span>
        </div>
      </div>
      <div class="row">
        <div class="form-group col-md-6">
          <button id="check-availability" type="button" class="btn btn-primary">Check Name Availability</button>
        </div>
      </div>  
    </div>
  </div>

  <div id="package" class="container">
    <div class="well well-md">
      <h4><b>Specify your visualization package</b></h4>
      <div class="container">
        <form id="checks" class="form-horizontal">
          <div class="checkbox">
            <label><input type="checkbox" id="location" name="optcheck" value="location">Location</label>
          </div>
          <div class="checkbox">
            <label><input type="checkbox" id="property" name="optcheck" value="property">Property</label>
          </div>
          <div class="checkbox">
            <label><input type="checkbox" id="market" name="optcheck" value="market">Market Trends</label>
          </div>
        </form>
        <form id="custom" class="form-horizontal">
         <div class="row">
            <div class="form-group col-md-2">
              <label for="usr">Custom Package</label>
              <input type="text" class="form-control" id="custom_form" placeholder="" value="">
              <span class="" for="usr" aria-hidden="true"></span>
            </div>
          </div>
        </div>
      </form>
    </div>
  </div>

  <div id="prefs" class="container">
    <div class="well well-md">
      <h4><b>Specify your customization preferences</b></h4>
      <div class="container">
        <form id="checks" class="form-horizontal">
          <div class="checkbox">
            <label><input type="checkbox" id="title" value="">Title</label>
          </div>
          <div class="checkbox">
            <label><input type="checkbox" id="native" value="">Native Background Integration</label>
          </div>
          <div class="checkbox">
            <label><input type="checkbox" id="footer" value="">Graphiq Footer Icon</label>
          </div>
          <div class="checkbox">
            <label><input type="checkbox" id="sources" value="">Data Source Citation</label>
          </div>
          <div class="checkbox">
            <label><input type="checkbox" id="share" value="">Share Button</label>
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
      <p>Review your preferences and submit the form. The API Key will be sent to the e-mail address listed below.</p>
      <div class="row">  
          <div class="form-group col-md-6">
            <label for="email">E-mail</label>
            <input type="email" class="form-control" id="email" placeholder="mrybak@graphiq.com" value="">
          </div>
      </div>
      <button id="submit-button" type="submit" class="btn btn-warning btn-block">Submit</button>
    </div>
  </div>
</form>
</body>
</html>

  
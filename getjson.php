<?php

	if ($_SERVER['REQUEST_METHOD'] == 'POST'){
	  $data = json_decode(file_get_contents("php://input"));
	  #file_put_contents('index.html', file_get_contents("php://input"));
	  	$usr = $data->originalRequest->data->sender->id;
		$src = $data->result->parameters->source->city;
		$dest = $data->result->parameters->destination;
		$cat = $data->result->metadata->intentName;
		$date = $data->timestamp;
		$sessionid = $data->sessionId;
		$json_response = array('userid' => $usr, 'sessionid'=> $sessionid, 'source' => $src, 'destination' => $dest, 'category' => $cat, 'date' => $date );
		header("Content-Type: application/json");
		echo json_encode($json_response);
		file_put_contents('index.html', json_encode($json_response));
		exec('chmod u+x python > phpout');
		#exec('python python/ridr.py '.$usr." ".$src." ".$dest." ".$date." ".$cat." ".$sessionid);
	}

?>
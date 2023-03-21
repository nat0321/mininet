service {
  name = "onos2"
  id = "onos2"
  address = "10.5.0.5"
  port = 6653

  tags      = ["v1"]
  meta      = {
    version = "1"
  }
  
  connect { 
    sidecar_service {
      port = 20000
      
      check {
        name = "Connect Envoy Sidecar"
        tcp = "10.5.0.4:20000"
        interval ="10s"
      }
    }  
  }
}

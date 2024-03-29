service {
  name = "web"
  id = "web-v1"
  address = "10.5.0.3"
  port = 6555
  
  connect { 
    sidecar_service {
      port = 20000
      
      check {
        name = "Connect Envoy Sidecar"
        tcp = "10.5.0.3:20000"
        interval ="10s"
      }

      proxy {
        upstreams {
          destination_name = "payments"
          local_bind_address = "127.0.0.1"
          local_bind_port = 6555
        }
        upstreams {
          destination_name = "onos2"
          local_bind_address = "127.0.0.1"
          local_bind_port = 6554
        }
      }
    }  
  }
}

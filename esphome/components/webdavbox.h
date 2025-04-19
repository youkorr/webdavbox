#pragma once

#include "esphome/core/component.h"
#include "esphome/components/web_server_base/web_server_base.h"
#include <vector>
#include <SD_MMC.h>
#include <FS.h>

namespace esphome {
namespace webdav {

class WebDavBox : public Component, public AsyncWebHandler {
 public:
  WebDavBox();
  
  void setup() override;
  void loop() override;
  void dump_config() override;
  float get_setup_priority() const override { return setup_priority::AFTER_WIFI; }

  void set_port(uint16_t port) { this->port_ = port; }
  void set_mount_point(const std::string &mount_point) { this->mount_point_ = mount_point; }
  void set_auth_enabled(bool auth_enabled) { this->auth_enabled_ = auth_enabled; }
  void set_username(const std::string &username) { this->username_ = username; }
  void set_password(const std::string &password) { this->password_ = password; }
  
  // SD card pin configuration
  void set_sd_dat0_pin(int pin) { this->sd_dat0_pin_ = pin; }
  void set_sd_dat1_pin(int pin) { this->sd_dat1_pin_ = pin; }
  void set_sd_dat2_pin(int pin) { this->sd_dat2_pin_ = pin; }
  void set_sd_dat3_pin(int pin) { this->sd_dat3_pin_ = pin; }
  void set_sd_cmd_pin(int pin) { this->sd_cmd_pin_ = pin; }
  void set_sd_clk_pin(int pin) { this->sd_clk_pin_ = pin; }

  bool canHandle(AsyncWebServerRequest *request) override;
  void handleRequest(AsyncWebServerRequest *request) override;
  void handleOptions(AsyncWebServerRequest *request);
  void handlePropfind(AsyncWebServerRequest *request);
  void handleGet(AsyncWebServerRequest *request);
  void handlePut(AsyncWebServerRequest *request);
  void handleDelete(AsyncWebServerRequest *request);
  void handleMkcol(AsyncWebServerRequest *request);
  void handleMove(AsyncWebServerRequest *request);
  
 protected:
  bool check_auth(AsyncWebServerRequest *request);
  bool init_sd_card();
  String get_content_type(const String &path);
  String url_to_path(const String &url);
  String escape_xml(const String &text);
  void send_xml_response(AsyncWebServerRequest *request, int code, const String &xml);
  String generate_propfind_response(const String &path, int depth);
  String generate_dir_xml(const String &path, const String &uri, int depth);
  String get_mime_type(const String &path);
  
  web_server_base::WebServerBase *base_{nullptr};
  uint16_t port_{80};
  std::string mount_point_{"/webdav"};
  bool auth_enabled_{true};
  std::string username_{"admin"};
  std::string password_{"admin"};
  

};

}  // namespace webdav
}  // namespace esphome

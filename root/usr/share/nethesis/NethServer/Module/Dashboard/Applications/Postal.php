<?php
namespace NethServer\Module\Dashboard\Applications;

/**
 * Nextcloud dashboard application widget
 *
 * @author Markus Neuberger
 */
class Postal extends \Nethgui\Module\AbstractModule implements \NethServer\Module\Dashboard\Interfaces\ApplicationInterface
{

    public function getName()
    {
        return "Postal";
    }

    public function getInfo()
    {
         // $host = explode(':',$_SERVER['HTTP_HOST']);
         $host = $this->getPlatform()->getDatabase('configuration')->getProp('postal', 'VirtualHost');

         return array(
            'url' => "https://".$host
         );
    }
}

<?php
namespace NethServer\Module\Dashboard\Applications;

/**
 * Postal dashboard application widget
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
         $host = "postal." + $this->getPlatform()->getDatabase('configuration')->getProp('postal', 'VirtualHost');
         if ($host == "") $host = "postal." + $this->getPlatform()->get('DomainName');
         return array(
            'url' => "https://".$host
         );
    }
}
